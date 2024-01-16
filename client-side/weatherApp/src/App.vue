<template>
  <div class="nav">
    <div id="text" class="luckiest-guy">
      Find My Weather
    </div>
  </div>
  <div>
    <input placeholder="Write your state code" class="input-bar" v-model="stateCode"/>
    <input placeholder="Write your city" class="input-bar2" v-model="city"/>
  </div>
  <button @click="submit" class="submit-button">Submit</button>
  <div class="card">
    <p class="cards" v-for="k in Object.keys(weather)">{{ k }} : {{ weather[k] }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return {
      stateCode: '',
      cirty: '',
      weather: {}
    }
  },
  methods: {
    async submit(){
      const request = await axios.post('http://localhost:5000', {'code': this.stateCode, 'city': this.city})
      this.weather = request.data
    }
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
  padding-bottom: 10%;
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
</style>
