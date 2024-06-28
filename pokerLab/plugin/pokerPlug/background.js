chrome.runtime.onMessage.addListener(() => {
  function(request, sender, message){
    if (request.message === "message"){
      console.log(message)
    }
  }
});
