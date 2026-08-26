<script>
  import { personalInfo } from '../data/portfolioData.js';
  import { showToast, copyToClipboard } from '../stores/toast.js';

  let name = '';
  let email = '';
  let subject = '';
  let message = '';

  function handleSubmit(e) {
    e.preventDefault();
    if (!name || !email || !message) {
      showToast('Please fill out all required fields.');
      return;
    }

    const sub = subject || 'Project Inquiry / Message';
    const mailtoUrl = `mailto:${personalInfo.email}?subject=${encodeURIComponent(sub)}&body=${encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`)}`;
    window.location.href = mailtoUrl;

    showToast('Opening your email client to send message...');
    name = ''; email = ''; subject = ''; message = '';
  }
</script>

<section class="contact-section" id="contact">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-paper-plane"></i> Get In Touch</span>
      <h2 class="section-title">Let's Build Something <span class="gradient-text">Extraordinary</span></h2>
      <p class="section-subtitle">Whether you need a custom Django backend, a lightning-fast Svelte interface, or full-stack consulting, I'm ready to collaborate.</p>
    </div>

    <div class="contact-grid">
      <div class="contact-info-panel glass-card">
        <h3 class="contact-panel-title"><i class="fas fa-address-card"></i> Contact Details</h3>
        <p class="contact-panel-desc">Reach out directly via email, WhatsApp, or order a verified escrow gig on Fiverr.</p>

        <div class="contact-methods">
          <div class="contact-method-item">
            <div class="method-icon"><i class="fas fa-envelope"></i></div>
            <div class="method-details">
              <span class="method-label">Direct Email</span>
              <a href="mailto:{personalInfo.email}" class="method-val">{personalInfo.email}</a>
            </div>
            <button class="copy-btn" on:click={() => copyToClipboard(personalInfo.email, 'Email')} title="Copy Email" aria-label="Copy Email">
              <i class="far fa-copy"></i>
            </button>
          </div>

          <div class="contact-method-item">
            <div class="method-icon"><i class="fab fa-whatsapp"></i></div>
            <div class="method-details">
              <span class="method-label">WhatsApp / Phone</span>
              <a href={personalInfo.whatsapp} target="_blank" rel="noopener noreferrer" class="method-val">{personalInfo.phone}</a>
            </div>
            <button class="copy-btn" on:click={() => copyToClipboard(personalInfo.phone, 'Phone Number')} title="Copy Phone" aria-label="Copy Phone">
              <i class="far fa-copy"></i>
            </button>
          </div>

          <div class="contact-method-item">
            <div class="method-icon"><i class="fas fa-bolt" style="color: #10b981;"></i></div>
            <div class="method-details">
              <span class="method-label">Fiverr Profile</span>
              <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="method-val">fiverr.com/{personalInfo.fiverrUsername}</a>
            </div>
          </div>

          <div class="contact-method-item">
            <div class="method-icon"><i class="fas fa-map-marker-alt"></i></div>
            <div class="method-details">
              <span class="method-label">Location</span>
              <span class="method-val">{personalInfo.location}</span>
            </div>
          </div>
        </div>

        <div class="contact-availability-box">
          <span class="avail-dot"></span>
          <span>Open for freelance contracts, full-time positions, and technical partnerships.</span>
        </div>
      </div>

      <div class="contact-form-panel glass-card">
        <h3 class="contact-panel-title"><i class="fas fa-envelope-open-text"></i> Send a Message</h3>
        <form on:submit={handleSubmit} class="contact-form" id="contact-form">
          <div class="form-group">
            <label for="form-name" class="form-label">Your Name *</label>
            <input type="text" id="form-name" class="form-input" placeholder="e.g. Alex Morgan" bind:value={name} required />
          </div>

          <div class="form-group">
            <label for="form-email" class="form-label">Your Email *</label>
            <input type="email" id="form-email" class="form-input" placeholder="e.g. alex@company.com" bind:value={email} required />
          </div>

          <div class="form-group">
            <label for="form-subject" class="form-label">Subject</label>
            <input type="text" id="form-subject" class="form-input" placeholder="e.g. Web App Development Project" bind:value={subject} />
          </div>

          <div class="form-group">
            <label for="form-message" class="form-label">Message *</label>
            <textarea id="form-message" class="form-textarea" placeholder="Tell me about your project scope, requirements, or timeline..." bind:value={message} required></textarea>
          </div>

          <button type="submit" class="btn btn-primary btn-glow" style="width: 100%; justify-content: center;">
            <i class="fas fa-paper-plane"></i> Send Message Directly
          </button>
        </form>
      </div>
    </div>
  </div>
</section>
