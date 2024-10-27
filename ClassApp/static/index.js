//TODO: Dark Mode
let theme_toggler = document.querySelector("#theme");
theme_toggler.addEventListener("click", () => {
  document.body.classList.toggle("dark");
});

const UpdateForm = () => {
  const Save = document.getElementById("Save");
  const Update = document.getElementById("Update");

  Save.checked
    ? document.getElementById("Form").setAttribute("method", "POST")
    : Update.checked
    ? document.getElementById("Form").setAttribute("method", "PUT")
    : null;
};
