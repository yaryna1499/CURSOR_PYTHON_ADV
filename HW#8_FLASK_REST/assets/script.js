function updateChargingProgress() {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "/get_value");
  xhr.onload = function () {
    if (xhr.status === 200) {
      const percentage = parseInt(xhr.responseText);
      const progressBar = document.querySelector(".progress");
      progressBar.style.width = `${percentage}%`;
      const val = document.querySelector(".percentage");
      const numberFrom = parseInt(val.innerHTML);
      let progress = numberFrom;
      const interval = setInterval(() => {
        if (numberFrom > percentage) {
          progress -= 1;
          if (progress <= percentage) {
            progress = percentage;
            clearInterval(interval);
          }
        } else {
          progress += 1;
          if (progress >= percentage) {
            progress = percentage;
            clearInterval(interval);
          }
        }

        const newVal = document.querySelector(".percentage");
        newVal.innerHTML = `${progress}%`;
      }, 500 / Math.abs(percentage - numberFrom));
    }
  };
  xhr.send();
}

setInterval(updateChargingProgress, 1000);
