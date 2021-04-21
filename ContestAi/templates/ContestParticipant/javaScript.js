$(document).ready(function () {
  // Enable Carousel Indicators
  $(".item1").click(function () {
    $("#carouselExampleIndicators").carousel(0);
  });
  $(".item2").click(function () {
    $("#carouselExampleIndicators").carousel(1);
  });
  $(".item3").click(function () {
    $("#carouselExampleIndicators").carousel(2);
  });

  const header = $("#headerPage");
  const templateHeader = {
    0: "Contest for Register",
    1: "Contest for Testing",
    2: "History Contest",
  };

  $("#carouselExampleIndicators").on("slide.bs.carousel", function (event) {
    const index = event.to;
    header.text(templateHeader[index]);
  });
});
