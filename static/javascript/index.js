// postImage = document.getElementById("post-image");
// nextButton = document.getElementById("next-button");
// previousButton = document.getElementById("previous-button");
// cardTitle = document.getElementById("card-title");

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function nextImage(button) {
  console.log(button);
  currentImage = button.parentElement.previousElementSibling.children[0];
  imageClassName = currentImage.className;
  imageClassList = imageClassName.split(" ");
  imageUrlsSource = imageUrlsCollection[Number(imageClassList[0])];
  currentImageUrlIndex = Number(imageClassList[1]);
  nextImageUrlIndex = currentImageUrlIndex + 1;

  if (nextImageUrlIndex <= imageUrlsSource.length - 1) {
    cardImage = currentImage.parentElement.parentElement;
    cardContent = cardImage.nextElementSibling;
    currentImageTitle = cardContent.children[0];

    console.log(
      String(imageClassList) +
        String(currentImageUrlIndex) +
        String(nextImageUrlIndex + " ----> ") +
        " , " +
        String(imageUrlsSource)
    );
    cardImage.style.height = "220px";
    cardContent.style.height = "130px";
    cardContent.style.paddingTop = "0";
    currentImageTitle.style.display = "block";

    // currentImageTitle = currentImage.parentElement.parentElement.nextElementSibling.children[0];
    currentImageTitle.innerHTML =
      "Image " +
      String(nextImageUrlIndex + 1) +
      " of " +
      String(imageUrlsSource.length);

    newImageSrc = imageUrlsSource[nextImageUrlIndex];
    // newImageSrc = imageUrlsCollection[Number(imageClassList[0])][Number(imageClassList[1]) + 1];
    currentImage.src = newImageSrc;
    // imageClassList = imageClassList.pop();
    // imageClassList = imageClassList.push(String(nextImageUrlIndex))
    currentImage.className =
      String(imageClassList[0]) + " " + String(nextImageUrlIndex);
  } else {
    nextImageUrlIndex -= 1;
    console.log(
      String(imageClassList) +
        String(currentImageUrlIndex) +
        String(nextImageUrlIndex + " ----> ") +
        " , " +
        String(imageUrlsSource)
    );
  }
}

function previousImage(button) {
  console.log(button);
  currentImage = button.parentElement.nextElementSibling.children[0];
  imageClassName = currentImage.className;
  imageClassList = imageClassName.split(" ");
  imageUrlsSource = imageUrlsCollection[Number(imageClassList[0])];
  currentImageUrlIndex = Number(imageClassList[1]);
  previousImageUrlIndex = currentImageUrlIndex - 1;

  cardImage = currentImage.parentElement.parentElement;
  cardContent = cardImage.nextElementSibling;
  currentImageTitle = cardContent.children[0];

  if (previousImageUrlIndex >= 0) {
    console.log(
      String(imageClassList) +
        String(currentImageUrlIndex) +
        String(previousImageUrlIndex + " ----> ") +
        " , " +
        String(imageUrlsSource)
    );
    if (previousImageUrlIndex === 0) {
      currentImageTitle.style.display = "none";
      cardImage.style.height = "250px";
      cardContent.style.height = "100px";
      cardContent.style.paddingTop = "12px";
    } else {
      cardImage.style.height = "220px";
      cardContent.style.height = "130px";
      cardContent.style.paddingTop = "0";
    }
    currentImageTitle.innerHTML =
      "Image " +
      String(previousImageUrlIndex + 1) +
      " of " +
      String(imageUrlsSource.length);
    newImageSrc = imageUrlsSource[previousImageUrlIndex];
    currentImage.src = newImageSrc;
    currentImage.className =
      String(imageClassList[0]) + " " + String(previousImageUrlIndex);
  } else {
    previousImageUrlIndex += 1;
    console.log(
      String(imageClassList) +
        String(currentImageUrlIndex) +
        String(previousImageUrlIndex + " ----> ") +
        " , " +
        String(imageUrlsSource)
    );
  }
}

function displayButtons(image) {
  UrlsSource = imageUrlsCollection[Number(image.classList[0])];
  imageTitle = image.parentElement.parentElement.nextElementSibling.children[0];

  imageClassName = image.className;
  imageClassList = imageClassName.split(" ");
  imageUrlIndex = Number(image.classList[1]);

  if (imageUrlIndex > 0) {
    imageTitle.style.display = "block";
  }

  if (UrlsSource.length > 1) {
    console.log(image);
    previousButton = image.parentElement.previousElementSibling.children[0];
    nextButton = image.parentElement.nextElementSibling.children[0];

    previousButton.style.display = "block";
    nextButton.style.display = "block";
  } else {
    console.log("ImageUrlSource's length is 1");
  }
}

function hideButtons(image) {
  imageTitle = image.parentElement.parentElement.nextElementSibling.children[0];
  previousButton = image.parentElement.previousElementSibling.children[0];
  nextButton = image.parentElement.nextElementSibling.children[0];

  imageTitle.style.display = "none";
  previousButton.style.display = "none";
  nextButton.style.display = "none";

  cardImage = image.parentElement.parentElement;
  cardContent = cardImage.nextElementSibling;

  cardImage.style.height = "250px";
  cardContent.style.height = "100px";
  cardContent.style.paddingTop = "12px";
}

function keepItemsVisible(button) {
  if (button.id === "previous-button") {
    secondButton =
      button.parentElement.nextElementSibling.nextElementSibling.children[0];
    image = button.parentElement.nextElementSibling.children[0];

    button.style.display = "block";
    secondButton.style.display = "block";
  } else if (button.id === "next-button") {
    secondButton =
      button.parentElement.previousElementSibling.previousElementSibling
        .children[0];
    image = button.parentElement.previousElementSibling.children[0];

    button.style.display = "block";
    secondButton.style.display = "block";
  }

  imageClassName = image.className;
  imageClassList = imageClassName.split(" ");
  imageUrlIndex = Number(image.classList[1]);

  if (imageUrlIndex > 0) {
    imageTitle =
      button.parentElement.parentElement.nextElementSibling.children[0];
    imageTitle.style.display = "block";
  }
}

function revertMouseOverEvent(button) {
  if (button.id === "previous-button") {
    secondButton =
      button.parentElement.nextElementSibling.nextElementSibling.children[0];

    button.style.display = "none";
    secondButton.style.display = "none";
  } else if (button.id === "next-button") {
    secondButton =
      button.parentElement.previousElementSibling.previousElementSibling
        .children[0];

    button.style.display = "none";
    secondButton.style.display = "none";
  }

  imageTitle =
    button.parentElement.parentElement.nextElementSibling.children[0];
  imageTitle.style.display = "none";
}

// function presentData() {
//   console.log("testing this");
//   console.log(data);
// }

// Image Title shows up on hovering over first image
// Two adjacent images have their buttons displayed at the same time
// Image Title changes before image does
