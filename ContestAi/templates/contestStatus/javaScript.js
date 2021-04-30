$(document).ready(function () {
  const getLinkFile = (path, modeFull = true) => {
    if (modeFull) return "../../../../" + path.split("/").slice(1).join("/");
    return path.split("/").pop();
  };
  $("#exampleModal").on("show.bs.modal", function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var recipient = button.data("whatever").replace(/\"/g, '$');
    recipient = recipient.replace(/\'/g,'"');

    const value = JSON.parse(recipient);
    console.log(value);
    console.log(getLinkFile(value.link), getLinkFile(value.link, false));
    var modal = $(this);
    modal.find(".modal-body #recipient-name").val(value.name);
    modal.find(".modal-body #recipient-time").val(value.time);
    modal.find(".modal-body #recipient-status").val(value.status);
    modal.find(".modal-body #recipient-language").val(value.language);
    modal.find(".modal-body #recipient-code").val(value.code.replace(/\$/g,'"'));
    modal
      .find(".modal-body #recipient-embed")
      .attr("src", getLinkFile(value.link));
    modal
      .find(".modal-body #recipient-download")
      .attr("href", getLinkFile(value.link));
    modal
      .find(".modal-body #recipient-download")
      .attr("download", getLinkFile(value.link, false));
  });
});
