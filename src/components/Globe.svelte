<script>
  import { onMount } from 'svelte';
  import { theme } from '../stores/theme.js';
  import { languagesData } from '../data/portfolioData.js';
  import { WORLD_LAND_POLYGONS } from '../data/worldData.js';

  let canvas;
  let sectionElement;
  let activeLang = languagesData[0];
  let isDragging = false;
  let hoveredFlag = null;
  let isVisibleInViewport = false;

  // Center on the Asia-Europe-Middle East region where the 7 languages are located
  let yaw = 45 * Math.PI / 180;
  let pitch = 22 * Math.PI / 180;
  let targetYaw = yaw;
  let targetPitch = pitch;
  let isTransitioning = false;
  let velYaw = 0;
  let velPitch = 0;
  let lastMouseX = 0;
  let lastMouseY = 0;
  let pulseTime = 0;

  function selectLanguage(lang) {
    activeLang = lang;
    targetYaw = lang.lon * Math.PI / 180;
    targetPitch = Math.max(-0.4, Math.min(0.5, lang.lat * Math.PI / 180 * 0.45));
    isTransitioning = true;
    velYaw = 0;
    velPitch = 0;
  }


  onMount(() => {
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let animId;

    let width = 480;
    let height = 480;
    let radius = 175;
    let dpr = window.devicePixelRatio || 1;

    function resize() {
      const rect = canvas.getBoundingClientRect();
      width = rect.width || 480;
      height = rect.height || 480;
      dpr = window.devicePixelRatio || 1;
      canvas.width = width * dpr;
      canvas.height = height * dpr;
      radius = Math.min(width, height) * 0.36;
    }
    resize();
    window.addEventListener('resize', resize);

    const graticuleLines = [];
    for (let lat = -60; lat <= 60; lat += 30) {
      const pts = [];
      for (let lon = -180; lon <= 180; lon += 8) pts.push({ lat, lon });
      graticuleLines.push(pts);
    }
    for (let lon = -180; lon < 180; lon += 45) {
      const pts = [];
      for (let lat = -80; lat <= 80; lat += 6) pts.push({ lat, lon });
      graticuleLines.push(pts);
    }

    function project(lat, lon, heightOffset = 0) {
      const radLat = lat * Math.PI / 180;
      const radLon = lon * Math.PI / 180;
      const r = radius + heightOffset;

      const cosLat = Math.cos(radLat);
      const sinLat = Math.sin(radLat);
      const deltaLon = radLon - yaw;

      const x0 = cosLat * Math.sin(deltaLon);
      const y0 = sinLat;
      const z0 = cosLat * Math.cos(deltaLon);

      const cosPitch = Math.cos(pitch);
      const sinPitch = Math.sin(pitch);

      const x = x0;
      const y = y0 * cosPitch - z0 * sinPitch;
      const z = y0 * sinPitch + z0 * cosPitch;

      const cx = (width * dpr) / 2;
      const cy = (height * dpr) / 2;

      return {
        x: cx + x * r * dpr,
        y: cy - y * r * dpr,
        z: z,
        visible: z > -0.15
      };
    }

    const onMouseDown = (e) => {
      isDragging = true;
      isTransitioning = false;
      lastMouseX = e.clientX;
      lastMouseY = e.clientY;
      velYaw = 0;
      velPitch = 0;
    };

    const onMouseUp = () => { isDragging = false; };

    const onMouseMove = (e) => {
      const rect = canvas.getBoundingClientRect();
      const mouseX = (e.clientX - rect.left) * dpr;
      const mouseY = (e.clientY - rect.top) * dpr;

      if (isDragging) {
        const dx = e.clientX - lastMouseX;
        const dy = e.clientY - lastMouseY;
        lastMouseX = e.clientX;
        lastMouseY = e.clientY;

        velYaw = dx * 0.006;
        velPitch = dy * 0.006;

        yaw -= velYaw;
        pitch = Math.max(-0.7, Math.min(0.7, pitch + velPitch));
      } else {
        let found = null;
        let minDist = Infinity;

        languagesData.forEach(lang => {
          const pHeight = lang.poleHeight || 32;
          const surface = project(lang.lat, lang.lon, 0);
          const tip = project(lang.lat, lang.lon, pHeight);

          if (surface.visible && surface.z > -0.1) {
            const offX = (lang.offsetX || 0) * dpr;
            const offY = (lang.offsetY || 0) * dpr;
            const targetX = tip.x + offX;
            const targetY = tip.y + offY;

            const dist = Math.hypot(mouseX - targetX, mouseY - targetY);
            if (dist < 32 * dpr && dist < minDist) {
              minDist = dist;
              found = lang;
            }
          }
        });

        if (found) {
          canvas.style.cursor = 'pointer';
          if (hoveredFlag !== found) {
            hoveredFlag = found;
            activeLang = found;
          }
        } else {
          canvas.style.cursor = isDragging ? 'grabbing' : 'grab';
          hoveredFlag = null;
        }
      }
    };

    const onTouchStart = (e) => {
      if (e.touches.length === 1) {
        isDragging = true;
        isTransitioning = false;
        lastMouseX = e.touches[0].clientX;
        lastMouseY = e.touches[0].clientY;
        velYaw = 0;
        velPitch = 0;
      }
    };

    const onTouchMove = (e) => {
      if (isDragging && e.touches.length === 1) {
        const dx = e.touches[0].clientX - lastMouseX;
        const dy = e.touches[0].clientY - lastMouseY;
        lastMouseX = e.touches[0].clientX;
        lastMouseY = e.touches[0].clientY;

        velYaw = dx * 0.007;
        velPitch = dy * 0.007;

        yaw -= velYaw;
        pitch = Math.max(-0.7, Math.min(0.7, pitch + velPitch));
      }
    };

    const onTouchEnd = () => { isDragging = false; };

    canvas.addEventListener('mousedown', onMouseDown);
    window.addEventListener('mouseup', onMouseUp);
    canvas.addEventListener('mousemove', onMouseMove);
    canvas.addEventListener('touchstart', onTouchStart, { passive: true });
    canvas.addEventListener('touchmove', onTouchMove, { passive: true });
    canvas.addEventListener('touchend', onTouchEnd);

    function render() {
      pulseTime += 0.04;

      if (isTransitioning) {
        let diffYaw = targetYaw - yaw;
        while (diffYaw < -Math.PI) diffYaw += Math.PI * 2;
        while (diffYaw > Math.PI) diffYaw -= Math.PI * 2;

        yaw += diffYaw * 0.08;
        pitch += (targetPitch - pitch) * 0.08;

        if (Math.abs(diffYaw) < 0.002 && Math.abs(targetPitch - pitch) < 0.002) {
          yaw = targetYaw;
          pitch = targetPitch;
          isTransitioning = false;
        }
      } else if (!isDragging && !hoveredFlag) {
        if (Math.abs(velYaw) > 0.0005) {
          yaw -= velYaw;
          velYaw *= 0.94;
        } else if (isVisibleInViewport) {
          yaw -= 0.0024;
        }

        if (Math.abs(velPitch) > 0.0005) {
          pitch = Math.max(-0.7, Math.min(0.7, pitch + velPitch));
          velPitch *= 0.94;
        }
      }

      const isLight = $theme === 'light';
      const globeBg = isLight ? '#eef2f6' : '#0b111e';
      const graticuleColor = isLight ? 'rgba(100, 116, 139, 0.08)' : 'rgba(148, 163, 184, 0.06)';
      const ringBorder = isLight ? 'rgba(96, 165, 250, 0.25)' : 'rgba(56, 189, 248, 0.2)';
      const landFill = isLight ? '#cbd5e1' : '#1e293b';
      const landStroke = isLight ? 'rgba(100, 116, 139, 0.35)' : 'rgba(96, 165, 250, 0.35)';

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const cx = (width * dpr) / 2;
      const cy = (height * dpr) / 2;
      const rScaled = radius * dpr;

      // 1. Ocean Sphere
      ctx.save();
      ctx.beginPath();
      ctx.arc(cx, cy, rScaled, 0, Math.PI * 2);
      ctx.fillStyle = globeBg;
      ctx.fill();

      const innerGrad = ctx.createRadialGradient(cx - rScaled * 0.3, cy - rScaled * 0.3, rScaled * 0.1, cx, cy, rScaled);
      if (isLight) {
        innerGrad.addColorStop(0, 'rgba(255, 255, 255, 0.7)');
        innerGrad.addColorStop(0.7, 'rgba(238, 242, 246, 0.85)');
        innerGrad.addColorStop(1, 'rgba(203, 213, 225, 0.5)');
      } else {
        innerGrad.addColorStop(0, 'rgba(24, 38, 64, 0.35)');
        innerGrad.addColorStop(0.7, 'rgba(11, 17, 30, 0.9)');
        innerGrad.addColorStop(1, 'rgba(6, 10, 18, 0.98)');
      }
      ctx.fillStyle = innerGrad;
      ctx.fill();

      ctx.lineWidth = 1.2 * dpr;
      ctx.strokeStyle = ringBorder;
      ctx.stroke();
      ctx.restore();

      // 2. Solid Vector Landmasses
      if (WORLD_LAND_POLYGONS && WORLD_LAND_POLYGONS.length > 0) {
        ctx.save();
        ctx.beginPath();
        ctx.arc(cx, cy, rScaled - 0.5 * dpr, 0, Math.PI * 2);
        ctx.clip();

        WORLD_LAND_POLYGONS.forEach(ring => {
          let started = false;
          ctx.beginPath();
          for (let i = 0; i < ring.length; i++) {
            const p = project(ring[i][0], ring[i][1], 0);
            if (p.visible && p.z > -0.05) {
              if (!started) {
                ctx.moveTo(p.x, p.y);
                started = true;
              } else {
                ctx.lineTo(p.x, p.y);
              }
            } else {
              started = false;
            }
          }
          ctx.fillStyle = landFill;
          ctx.fill();
          ctx.strokeStyle = landStroke;
          ctx.lineWidth = 1 * dpr;
          ctx.stroke();
        });
        ctx.restore();
      }

      // 3. Graticules
      ctx.save();
      ctx.lineWidth = 1 * dpr;
      ctx.strokeStyle = graticuleColor;
      graticuleLines.forEach(line => {
        ctx.beginPath();
        let isDrawing = false;
        line.forEach(pt => {
          const proj = project(pt.lat, pt.lon, 0);
          if (proj.visible && proj.z > 0) {
            if (!isDrawing) { ctx.moveTo(proj.x, proj.y); isDrawing = true; }
            else { ctx.lineTo(proj.x, proj.y); }
          } else { isDrawing = false; }
        });
        ctx.stroke();
      });
      ctx.restore();

      // 4. Sticking-out Flagpoles & Badges
      const projectedFlags = languagesData.map(lang => {
        const pHeight = lang.poleHeight || 32;
        const surface = project(lang.lat, lang.lon, 0);
        const tip = project(lang.lat, lang.lon, pHeight);
        const offX = (lang.offsetX || 0) * dpr;
        const offY = (lang.offsetY || 0) * dpr;
        return {
          lang,
          surface,
          tip,
          badgeCenter: { x: tip.x + offX, y: tip.y + offY },
          isActive: lang.id === activeLang.id,
          isHovered: hoveredFlag && hoveredFlag.id === lang.id
        };
      }).sort((a, b) => {
        if (a.isHovered || a.isActive) return 1;
        if (b.isHovered || b.isActive) return -1;
        return a.surface.z - b.surface.z;
      });

      projectedFlags.forEach(({ lang, surface, tip, badgeCenter, isActive, isHovered }) => {
        if (!surface.visible || surface.z < -0.1) return;

        const opacity = Math.max(0.2, Math.min(1, (surface.z + 0.1) * 2));
        ctx.save();
        ctx.globalAlpha = opacity;

        // Anchor Dot
        ctx.beginPath();
        ctx.arc(surface.x, surface.y, (isActive || isHovered ? 4 : 2.8) * dpr, 0, Math.PI * 2);
        ctx.fillStyle = isLight ? '#0284c7' : '#38bdf8';
        ctx.fill();

        if (isActive || isHovered) {
          ctx.beginPath();
          const pulseR = (5.5 + Math.sin(pulseTime * 3) * 2.5) * dpr;
          ctx.arc(surface.x, surface.y, pulseR, 0, Math.PI * 2);
          ctx.strokeStyle = isLight ? 'rgba(2, 132, 199, 0.45)' : 'rgba(56, 189, 248, 0.45)';
          ctx.lineWidth = 1.2 * dpr;
          ctx.stroke();
        }

        // Stem Line
        ctx.beginPath();
        ctx.moveTo(surface.x, surface.y);
        ctx.lineTo(tip.x, tip.y);
        if (badgeCenter.x !== tip.x || badgeCenter.y !== tip.y) {
          ctx.lineTo(badgeCenter.x, badgeCenter.y);
        }
        ctx.lineWidth = (isActive || isHovered ? 1.8 : 1.2) * dpr;
        const poleGrad = ctx.createLinearGradient(surface.x, surface.y, badgeCenter.x, badgeCenter.y);
        if (isLight) {
          poleGrad.addColorStop(0, '#0284c7');
          poleGrad.addColorStop(1, '#0d9488');
        } else {
          poleGrad.addColorStop(0, 'rgba(96, 165, 250, 0.7)');
          poleGrad.addColorStop(1, 'rgba(45, 212, 191, 0.85)');
        }
        ctx.strokeStyle = poleGrad;
        ctx.stroke();

        // Flag Badge
        const pillText = `${lang.flag} ${lang.name.split(' ')[0]}`;
        ctx.font = `600 ${Math.round(11 * dpr)}px sans-serif`;
        const textW = ctx.measureText(pillText).width;
        const padX = 8 * dpr;
        const padY = 4 * dpr;
        const pillW = textW + padX * 2;
        const pillH = 22 * dpr;
        const pillX = badgeCenter.x - pillW / 2;
        const pillY = badgeCenter.y - pillH / 2;

        ctx.beginPath();
        ctx.roundRect(pillX, pillY, pillW, pillH, 11 * dpr);

        if (isActive || isHovered) {
          ctx.fillStyle = isLight ? '#ffffff' : '#1e293b';
          ctx.fill();
          ctx.strokeStyle = isLight ? '#0284c7' : '#38bdf8';
          ctx.lineWidth = 1.8 * dpr;
          ctx.stroke();
          ctx.shadowColor = isLight ? 'rgba(2, 132, 199, 0.3)' : 'rgba(56, 189, 248, 0.35)';
          ctx.shadowBlur = 8 * dpr;
        } else {
          ctx.fillStyle = isLight ? 'rgba(255, 255, 255, 0.95)' : 'rgba(17, 24, 39, 0.9)';
          ctx.fill();
          ctx.strokeStyle = isLight ? 'rgba(0, 0, 0, 0.1)' : 'rgba(255, 255, 255, 0.12)';
          ctx.lineWidth = 1 * dpr;
          ctx.stroke();
        }

        ctx.shadowBlur = 0;
        ctx.fillStyle = isLight ? '#0f172a' : '#f1f5f9';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(pillText, badgeCenter.x, badgeCenter.y);
        ctx.restore();
      });

      animId = requestAnimationFrame(render);
    }

    let observer;
    if (typeof IntersectionObserver !== 'undefined' && sectionElement) {
      observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          isVisibleInViewport = entry.isIntersecting;
        });
      }, { threshold: 0.15 });
      observer.observe(sectionElement);
    } else {
      isVisibleInViewport = true;
    }

    render();

    return () => {
      cancelAnimationFrame(animId);
      if (observer) observer.disconnect();
      window.removeEventListener('resize', resize);
      window.removeEventListener('mouseup', onMouseUp);
      if (canvas) {
        canvas.removeEventListener('mousedown', onMouseDown);
        canvas.removeEventListener('mousemove', onMouseMove);
        canvas.removeEventListener('touchstart', onTouchStart);
        canvas.removeEventListener('touchmove', onTouchMove);
        canvas.removeEventListener('touchend', onTouchEnd);
      }
    };
  });
</script>

<section class="polyglot-section" id="languages" bind:this={sectionElement}>
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-globe-americas"></i> Polyglot Advantage</span>
      <h2 class="section-title">Global Reach Across <span class="gradient-text">7 Languages</span></h2>
      <p class="section-subtitle">Interact with the 3D globe to explore language proficiency, native greetings, and cultural hubs.</p>
    </div>

    <div class="globe-layout">
      <div class="globe-visual-wrapper glass-card">
        <div class="globe-container">
          <div class="globe-atmosphere"></div>
          <canvas bind:this={canvas} id="globe-canvas" width="600" height="600"></canvas>
          <div class="globe-instruction-tag">
            <i class="fas fa-arrows-alt"></i> <span>Drag to rotate globe • Hover flags to explore</span>
          </div>
        </div>
      </div>

      <div class="globe-sidebar">
        <div class="globe-detail-card glass-card" id="globe-detail-card">
          <div class="detail-header">
            <div class="detail-flag-badge">{activeLang.flag}</div>
            <div>
              <h3 class="detail-lang-name">{activeLang.name}</h3>
              <span class="detail-level-tag {activeLang.levelClass}">{activeLang.level}</span>
            </div>
            <span class="detail-region-tag"><i class="fas fa-map-marker-alt"></i> {activeLang.region}</span>
          </div>

          <div class="detail-greeting-display">
            <div class="detail-script-title">Native Greeting</div>
            <div class="detail-greeting-script lang-{activeLang.id}" class:rtl={activeLang.isRTL}>{activeLang.greeting}</div>
            <div class="detail-greeting-translit">{activeLang.translit}</div>
          </div>

          <p class="detail-desc">{activeLang.desc}</p>
        </div>

        <div class="globe-lang-selector-title">
          <i class="fas fa-compass"></i> Focus Language Location
        </div>
        <div class="globe-lang-pills">
          {#each languagesData as lang}
            <button 
              class="globe-pill" 
              class:active={activeLang.id === lang.id}
              on:click={() => selectLanguage(lang)}
            >
              <span>{lang.flag} {lang.name.split(' ')[0]}</span>
              <span class="pill-badge">{lang.level}</span>
            </button>
          {/each}
        </div>
      </div>
    </div>
  </div>
</section>

<style>
  .detail-greeting-script.lang-malayalam {
    font-family: 'Anek Malayalam', -apple-system, BlinkMacSystemFont, 'Outfit', sans-serif;
    font-weight: 700;
    letter-spacing: 0.5px;
  }
  .detail-greeting-script.lang-hindi {
    font-family: 'Anek Devanagari', -apple-system, BlinkMacSystemFont, 'Outfit', sans-serif;
  }
  .detail-greeting-script.lang-arabic,
  .detail-greeting-script.lang-urdu {
    font-family: 'Amiri', serif;
    font-size: 2.35rem;
  }
</style>

