<template>
<div class="chatBox">
  <div v-for="qaPair in qaPairs" :key="qaPair.question" class="qaPair">
    <p><b>Question:</b> {{ qaPair.question }}</p>
    <p><b>Answer:</b> {{ qaPair.answer }}</p>
  </div>
    <div>
    <input v-model="question"/>
    <button @click="getAnswer">Click</button>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
export default {
    
    props: ['weather'],
    data(){
    return {
      question: '',
      qaPairs: [],
    }
  },
  methods: {
    async getAnswer(){  
      let temp
      if (parseInt(this.weather['feels_like']) < 70){
        temp = '60<'
      } else if (parseInt(this.weather['feels_like']) > 70){
        temp = '60>'
      }
      const request = await axios.post('http://localhost:5000/query', {'question': this.question, 'weather': this.weather['description'], 'temp': temp})
      this.qaPairs.push({ 
        question: this.question, 
        answer: request.data // Assuming the response contains an 'answer' field
      });
      this.answer = request.data
      this.question = ''
    }
  }
}
</script>