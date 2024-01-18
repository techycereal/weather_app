<template>
<div v-if="loading === false" class='center-container'> 
    <div class="weather-card" >
      <div class='weather-icon'>
        <img :src="image"/>
      </div>
        <div class='temperature'>{{parseInt(weather['temp'])}}</div>
        <div class='weather-info'>
          <div class='weather-condition'>{{weather['description']}}</div>
          <div class='weather-stats'>
            <div class='feels-like'>Feels like: {{parseInt(weather['feels_like'])}}</div>
            <div class='temp_max'>Temp Max: {{parseInt(weather['temp_max'])}}</div>
            <div class='temp_min'>Temp Min: {{parseInt(weather['temp_min'])}}</div>
            <div class='wind'>Wind: {{parseInt(weather['wind'])}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default{
  props: ['weather', 'loading', 'image']
}
</script>