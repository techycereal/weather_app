<template>
<div class="nav">
    <div id="text" class="luckiest-guy">
      Find My Weather
    </div>
  </div>
</template>
<script>
export default {
    props: ['loading']
}
</script>

<style>
@keyframes float {
    0% {
        transform: translate(100, 100);
    }
    10% {
        transform: translate(10vw, -30px);
    }
    20% {
        transform: translate(20vw, 30px);
    }
    30% {
        transform: translate(30vw, -30px);
    }
    40% {
        transform: translate(40vw, 30px);
    }
    50% {
        transform: translate(50vw, -30px);
    }
    60% {
        transform: translate(60vw, 30px);
    }
    70% {
        transform: translate(70vw, -30px);
    }
    80% {
        transform: translate(80vw, 30px);
    }
    90% {
        transform: translate(90vw, -30px);
    }
    100% {
        transform: translate(100vw, 0);
    }
}

.floating {
    animation: float 7s linear infinite;
}
</style>