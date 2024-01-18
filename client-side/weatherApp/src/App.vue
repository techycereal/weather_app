<template>
  <Header/>
  <div>
    <input placeholder="Write your state code" class="input-bar" v-model="stateCode"/>
    <input placeholder="Write your city" class="input-bar2" v-model="city"/>
    <button @click="submit" class="submit-button">Submit</button>
  </div>
  <WeatherCard :weather="weather" :loading="loading" :image="image"/>
  <EnterInfo :weather="weather"/>
  <div v-if="loading === true" class="animationdiv">
  <img src="https://storesimages.blob.core.windows.net/images/misc/current/cloud.png" :class="{ floating: loading }"/>
  <p style="textAlign: center; fontSize: 100px">Loading</p>
  </div>

  
</template>

<script>
import axios from 'axios'
import images from '../images.json'
import WeatherCard from './components/WeatherCard.vue'
import EnterInfo from './components/EnterInfo.vue'
import Header from './components/Header.vue'
export default {
  components: {
    WeatherCard,
    EnterInfo,
    Header
  },
  data(){
    return {
      weather: {},
      loading: null,
      image: ''
    }
  },
  methods: {
    async submit(){
      
      this.loading = true
      const request = await axios.post('http://localhost:5000', {'code': this.stateCode, 'city': this.city})
      this.weather = request.data
      this.image = images['images'][this.weather['description']]
      this.startLoading()
    },
    startLoading(){
      setTimeout(() => {
        this.loading = false
      }, 4000);
    },
  }

}
</script>
 
<style>
html, body {
  background-color: #75AED6; /* Replace 'your-color' with your desired background color */
  margin: 0; /* Remove any default margin */
  padding: 0; /* Remove any default padding */
}
.nav {
  position: fixed; /* Make the header fixed at the top */
  top: 0; /* Align it to the top of the screen */
  left: 0;
  right: 0;
  background-color: #3C5097;
  color: white;
  text-align: center;
  font-size: 30px;
  padding: 50px 0; /* Adjust padding as needed */
  margin: 0; /* Remove any default margin */
  z-index: 1000; /* Ensure it's above other content */
}
.luckiest-guy {
  font-family: 'Luckiest Guy', cursive; /* Use the 'Luckiest Guy' font */
  font-weight: 800;
  font-size: 170%;
  color: #A7DCDC;
}
.input-bar2,
.input-bar{
  margin-top: 10%;
  margin-left: 43%;
  height: 40px;
  font-size: 20px;
  width: 13%;
  border-radius: 15px;
  border: none;
}
.input-bar2 {
  margin-top: 1%;
}
.card {
  background-color: white;
  margin-top: 6%;
  width: 13%;
  margin-left: 43%;
  border-radius: 15px;
}
.cards{
  margin: 0;
}
.submit-button {
  border-radius: 5px;
  border: none;
  width: 7%;
  font-size: 120%;
  padding-top: .25%;
  padding-bottom: .25%;
  margin-top: 1%;
  margin-left: 46%;
  background-color: white;
}

.animationdiv {
  margin-top: 50px;
  margin-left: 60px
}
.chatBox {
  position: fixed; /* Fix the position relative to the viewport */
  bottom: 10px;    /* Position from the bottom */
  right: 10px;     /* Position from the right */
  width: 300px;    /* Set a fixed width */
  max-height: 400px; /* Set a maximum height */
  background-color: white;
  padding: 10px;
  border-radius: 15px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* Optional: Adds a shadow for better visibility */
  overflow-y: auto; /* Enables scrolling if content overflows */
  z-index: 1000; /* Ensure it's above other content */
}

.center-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 30vh; /* This will take the full height of the viewport */
  width: 100vw; /* This will take the full width of the viewport */
}

.weather-card {
  width: 250px;
  padding: 20px;
  background-color: #E4E3E3;
  border-radius: 15px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  text-align: center;
}

.weather-icon {
  margin-bottom: 10px;
}

.weather-icon img {
  width: 50px;
  height: auto;
}

.temperature {
  font-size: 2.5em;
  font-weight: bold;
  margin-bottom: 10px;
}

.weather-info {
  border-top: 1px solid #e0e0e0;
  padding-top: 10px;
}

.weather-condition {
  font-size: 1.2em;
  margin-bottom: 10px;
}

.weather-stats div {
  font-size: 0.9em;
  margin-bottom: 5px;
}

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
