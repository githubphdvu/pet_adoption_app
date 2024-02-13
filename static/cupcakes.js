const BASE_URL = "http://127.0.0.1:5000/api"
function generateCupcakeHTML(cupcake) {//given a cupcake data,generate html
  return `
    <div data-cupcake-id=${cupcake.id}>
        <li>
            ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
            <button class="delete-button">Delete</button>
        </li>
        <img class="Cupcake-img" src="${cupcake.image}">
    </div>
    `
}
async function showInitialCupcakes() {//put initial cupcakes on page
    const response = await axios.get(`${BASE_URL}/cupcakes`)
    for (let cupcakeData of response.data.cupcakes) {
        let newCupcake = $(generateCupcakeHTML(cupcakeData))
        $("#cupcakes-list").append(newCupcake);
    }
}
$("#new-cupcake-form").on("submit", async function (evt) {//handle form for adding of new cupcakes
    evt.preventDefault()
    let flavor = $("#form-flavor").val()
    let rating = $("#form-rating").val()
    let size = $("#form-size").val()
    let image = $("#form-image").val()
    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`,{flavor,rating,size,image})
    let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake))
    $("#cupcakes-list").append(newCupcake)
    $("#new-cupcake-form").trigger("reset")
})
$("#cupcakes-list").on("click", ".delete-button", async function (evt) {//handle clicking delete: delete cupcake
  evt.preventDefault()
  let $cupcake = $(evt.target).closest("div")
  let cupcakeId = $cupcake.attr("data-cupcake-id")
  await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`)
  $cupcake.remove()
})
$(showInitialCupcakes)