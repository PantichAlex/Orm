<template lang="pug">
    #app
      .container
        .sights(v-if="sights.loaded")
          .items
            .item(v-for="sight in sights.items")
              .item_name Название: {{sight.name}}
              .item_year Год открытия: {{sight.year | yearFilter}}
              .item_desc Описание: {{sight.description}}
              .item_state Область: {{sight.state.name}}
              .item_country Страна: {{sight.state.country}}
        .loding(v-else) загрузка



</template>

<script>


export default {
  name: 'App',
  data(){
    return {
      sights:{
        loaded: false,

        items:[]
      }
    }
  },
  methods:{
   async loadSights(){

    try{
      let sights=await fetch("/api/sight").then((responce)=>responce.json());
      for(let sight in sights){

            
            this.sights.items.push(sights[sight]);

        
       }
        this.sights.loaded=true;
    
    }catch(exeption){
      this.sights.loaded=false;
    }

   }
  },
  filters: {
    yearFilter(year){

      if(year<0){

        return Math.abs(year)+" до н.э.";
      }

      return year;
    }
  },
  mounted() {
    this.loadSights()
 }
}
</script>

<style lang="sass" scoped>

  .container
    display: flex
    justify-content: center
    .sights
      width: 60%
      .items

        

        .item
          &+&
          margin-top: 5px
          background-color: darken(#fff, 10%)
          border-radius: 25px
          padding: 30px
          &_name
          &_year
          &_desc 
    .loading

</style>
