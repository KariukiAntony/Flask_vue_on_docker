<template>
  <div>
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            <strong>{{ message }}</strong>
        </div>
        <br>
    </div>
</template> 


<script>
export default {
  props: ["message"],
};
</script>
