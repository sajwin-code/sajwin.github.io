<script>
  import { currency, toggleCurrency } from '../stores/currency.js';
  import { pricingPackages, comparisonMatrix, personalInfo } from '../data/portfolioData.js';

  let showComparison = false;

  function toggleComparisonTable() {
    showComparison = !showComparison;
  }
</script>

<section class="pricing-section" id="pricing">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-tag"></i> Packages & Pricing</span>
      <h2 class="section-title">Transparent Plans & <span class="gradient-text">Development Packages</span></h2>
      <p class="section-subtitle">Secure freelance orders backed by Fiverr Escrow Buyer Protection. Custom scopes also available upon request.</p>
    </div>

    <div class="currency-toggle-wrapper">
      <span class="currency-label" class:active={$currency === 'INR'}>₹ INR (India)</span>
      <button class="currency-switch-btn" on:click={toggleCurrency} aria-label="Switch Currency">
        <span class="currency-thumb" class:usd={$currency === 'USD'}></span>
      </button>
      <span class="currency-label" class:active={$currency === 'USD'}>$ USD (Global)</span>
    </div>

    <div class="pricing-grid">
      {#each pricingPackages as pkg}
        <div class="pricing-card glass-card" class:popular={pkg.popular}>
          {#if pkg.popular}
            <div class="popular-badge"><i class="fas fa-fire"></i> Most Popular</div>
          {/if}

          <div class="package-tier-name">{pkg.name}</div>
          <h3 class="package-title">{pkg.title}</h3>
          <p class="package-desc">{pkg.description}</p>

          <div class="package-price-box">
            <span class="price-starting-tag">Starting from</span>
            <div class="price-val">
              {#if $currency === 'INR'}
                <span class="currency-sym">₹</span>{pkg.priceINR.toLocaleString('en-IN')}
              {:else}
                <span class="currency-sym">$</span>{pkg.priceUSD}
              {/if}
            </div>
          </div>

          <div class="package-meta-badges">
            <div class="meta-badge"><i class="fas fa-clock"></i> {pkg.deliveryDays} Days Delivery</div>
            <div class="meta-badge"><i class="fas fa-sync-alt"></i> {pkg.revisions} Revisions</div>
            <div class="meta-badge"><i class="fas fa-file-code"></i> {pkg.pages} Pages</div>
          </div>

          <ul class="package-features-list">
            {#each pkg.features as feat}
              <li class:excluded={!feat.included}>
                <i class={feat.included ? "fas fa-check-circle feat-check" : "fas fa-minus-circle feat-cross"}></i>
                <span>{feat.text}</span>
              </li>
            {/each}
          </ul>

          <a href={pkg.fiverrLink} target="_blank" rel="noopener noreferrer" class="btn btn-package" class:btn-primary={pkg.popular} class:btn-outline={!pkg.popular}>
            <i class="fas fa-bolt"></i> Order on Fiverr
          </a>
        </div>
      {/each}
    </div>

    <div class="comparison-toggle-box">
      <button class="btn btn-outline" on:click={toggleComparisonTable}>
        <i class={showComparison ? "fas fa-chevron-up" : "fas fa-table"}></i>
        {showComparison ? "Hide Detailed Comparison Matrix" : "View Full Feature Comparison Table"}
      </button>
    </div>

    {#if showComparison}
      <div class="comparison-table-wrapper glass-card">
        <table class="comparison-table">
          <thead>
            <tr>
              <th class="th-feature">Package Deliverables</th>
              <th class="th-tier">BASIC<br><span class="th-price">{$currency === 'INR' ? '₹6,999' : '$80'}</span></th>
              <th class="th-tier popular-col">STANDARD<br><span class="th-price">{$currency === 'INR' ? '₹14,999' : '$180'}</span></th>
              <th class="th-tier">PREMIUM<br><span class="th-price">{$currency === 'INR' ? '₹29,999' : '$350'}</span></th>
            </tr>
          </thead>
          <tbody>
            {#each comparisonMatrix as row}
              <tr>
                <td class="td-feature">{row.feature}</td>
                
                <td class="td-val">
                  {#if typeof row.basic === 'boolean'}
                    <i class={row.basic ? "fas fa-check-circle table-check" : "fas fa-minus table-minus"}></i>
                  {:else}
                    <span class="table-text">{row.basic}</span>
                  {/if}
                </td>

                <td class="td-val popular-col">
                  {#if typeof row.standard === 'boolean'}
                    <i class={row.standard ? "fas fa-check-circle table-check" : "fas fa-minus table-minus"}></i>
                  {:else}
                    <span class="table-text">{row.standard}</span>
                  {/if}
                </td>

                <td class="td-val">
                  {#if typeof row.premium === 'boolean'}
                    <i class={row.premium ? "fas fa-check-circle table-check" : "fas fa-minus table-minus"}></i>
                  {:else}
                    <span class="table-text">{row.premium}</span>
                  {/if}
                </td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    {/if}

    <div class="fiverr-trust-banner glass-card">
      <div class="trust-content">
        <div class="trust-icon"><i class="fas fa-shield-alt"></i></div>
        <div>
          <h4 class="trust-title">Secure Milestone Orders via Fiverr Escrow</h4>
          <p class="trust-p">Payments are safely held in escrow by Fiverr and only released upon your 100% satisfaction and delivery approval.</p>
        </div>
      </div>
      <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="btn btn-fiverr-trust">
        <i class="fas fa-external-link-alt"></i> Visit @sajwin_sj on Fiverr
      </a>
    </div>
  </div>
</section>

<style>
  .pricing-section {
    background: var(--bg-secondary);
    position: relative;
  }
  .currency-toggle-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 3rem;
  }
  .currency-label {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text-muted);
    transition: var(--transition);
  }
  .currency-label.active {
    color: var(--primary);
  }
  .currency-switch-btn {
    width: 58px;
    height: 32px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-full);
    position: relative;
    cursor: pointer;
    padding: 3px;
    transition: var(--transition);
  }
  .currency-thumb {
    display: block;
    width: 24px;
    height: 24px;
    background: var(--primary);
    border-radius: 50%;
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }
  .currency-thumb.usd {
    transform: translateX(26px);
  }
  .pricing-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    margin-bottom: 2.5rem;
    align-items: stretch;
  }
  .pricing-card {
    padding: 2.25rem 2rem;
    display: flex;
    flex-direction: column;
    position: relative;
    border-radius: var(--radius-lg);
    transition: var(--transition);
  }
  .pricing-card.popular {
    border-color: var(--primary);
    box-shadow: 0 8px 30px var(--primary-glow);
    transform: scale(1.03);
    z-index: 2;
  }
  .popular-badge {
    position: absolute;
    top: -14px;
    left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: #ffffff;
    font-size: 0.75rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 0.35rem 1rem;
    border-radius: var(--radius-full);
    box-shadow: 0 4px 12px var(--primary-glow);
  }
  .package-tier-name {
    font-size: 0.8rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--primary);
    margin-bottom: 0.5rem;
  }
  .package-title {
    font-size: 1.35rem;
    font-weight: 800;
    margin-bottom: 0.75rem;
    color: var(--text-primary);
  }
  .package-desc {
    font-size: 0.88rem;
    color: var(--text-secondary);
    line-height: 1.5;
    margin-bottom: 1.5rem;
    min-height: 48px;
  }
  .package-price-box {
    margin-bottom: 1.5rem;
    padding-bottom: 1.25rem;
    border-bottom: 1px solid var(--border-color);
  }
  .price-starting-tag {
    font-size: 0.75rem;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 1px;
    color: var(--text-muted);
    display: block;
    margin-bottom: 0.25rem;
  }
  .price-val {
    font-size: 2.4rem;
    font-weight: 900;
    color: var(--text-primary);
    font-family: var(--font-heading);
    line-height: 1.1;
  }
  .currency-sym {
    font-size: 1.6rem;
    color: var(--primary);
    margin-right: 2px;
  }
  .package-meta-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
  }
  .meta-badge {
    font-size: 0.75rem;
    font-weight: 700;
    padding: 0.25rem 0.65rem;
    border-radius: var(--radius-sm);
    background: var(--bg-main);
    color: var(--text-secondary);
    border: 1px solid var(--border-color);
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
  }
  .package-features-list {
    list-style: none;
    margin-bottom: 2rem;
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
    flex-grow: 1;
  }
  .package-features-list li {
    font-size: 0.88rem;
    display: flex;
    align-items: center;
    gap: 0.65rem;
    color: var(--text-primary);
  }
  .package-features-list li.excluded {
    color: var(--text-muted);
    opacity: 0.65;
  }
  .feat-check { color: #10b981; }
  .feat-cross { color: var(--text-muted); opacity: 0.6; }
  .btn-package {
    width: 100%;
    justify-content: center;
  }
  .comparison-toggle-box {
    text-align: center;
    margin-bottom: 2rem;
  }
  .comparison-table-wrapper {
    overflow-x: auto;
    padding: 1.5rem;
    border-radius: var(--radius-lg);
    margin-bottom: 2.5rem;
  }
  .comparison-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
  }
  .comparison-table th, .comparison-table td {
    padding: 1rem 1.25rem;
    border-bottom: 1px solid var(--border-color);
  }
  .th-feature, .td-feature {
    text-align: left;
    font-weight: 600;
    color: var(--text-primary);
  }
  .th-tier, .td-val {
    text-align: center;
    width: 22%;
  }
  .th-price {
    font-size: 1.1rem;
    font-weight: 800;
    color: var(--primary);
  }
  .popular-col {
    background: rgba(56, 189, 248, 0.04);
  }
  .table-check { color: #10b981; font-size: 1.1rem; }
  .table-minus { color: var(--text-muted); opacity: 0.5; }
  .table-text { font-weight: 700; color: var(--text-primary); }
  .fiverr-trust-banner {
    padding: 1.75rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1.5rem;
    flex-wrap: wrap;
    border-radius: var(--radius-lg);
  }
  .trust-content {
    display: flex;
    align-items: center;
    gap: 1.25rem;
  }
  .trust-icon {
    font-size: 2.2rem;
    color: #10b981;
  }
  .trust-title {
    font-size: 1.15rem;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 0.25rem;
  }
  .trust-p {
    font-size: 0.88rem;
    color: var(--text-secondary);
  }
  .btn-fiverr-trust {
    background: #10b981;
    color: #ffffff;
    padding: 0.75rem 1.5rem;
    font-weight: 700;
    border-radius: var(--radius-full);
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: var(--transition);
  }
  .btn-fiverr-trust:hover {
    background: #059669;
    box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
    transform: translateY(-2px);
  }
  @media (max-width: 1024px) {
    .pricing-grid {
      grid-template-columns: 1fr;
    }
    .pricing-card.popular {
      transform: none;
    }
  }
</style>
