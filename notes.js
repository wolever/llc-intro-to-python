jQuery(function() {
  var $ = jQuery;
  var showNotes = !!window.location.toString().match(/notes=[^0]/);
  if (!showNotes)
    return;

  $("aside.notes")
    .each(function() {
      var $this = $(this);
      $this
        .css("display", "block")
        .append("<i class='show-hide fa fa-arrow-down'></i>");
    })
    .on("click", ".show-hide", function() {
      var $this = $(this);
      var $parent = $this.parents("aside.notes");

      $this
        .toggleClass("fa-arrow-down")
        .toggleClass("fa-arrow-up")

      $parent
        .toggleClass("lowered")
    });
});
