<script>
  import { toast } from '../stores/toast.js';
</script>

<div class="toast-container" class:show={$toast.visible} id="toast">
  <i class="fas fa-check-circle"></i>
  <span id="toast-message">{$toast.message}</span>
</div>
