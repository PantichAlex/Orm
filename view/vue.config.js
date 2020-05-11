const path = require("path");

module.exports = {

	 // css: {
	 //    loaderOptions: {
	 //      sass: {

	 //        data: `@import "~@/assets/_main.sass`
	 //      }
	 //    }
	 //  },
	  devServer:{
	  	proxy: 'http://localhost:5000'
	  }
}