// Когда html документ готов (прорисован)
$(document).ready(function () {
// // При клике по значку корзины открываем всплывающее(модальное) окно
// $('#modalButton').click(function () {
//     $('#exampleModal').appendTo('body');

//     $('#exampleModal').modal('show');
// });

// // Событите клик по кнопке закрыть окна корзины
// $('#exampleModal .btn-close').click(function () {
//     $('#exampleModal').modal('hide');
// });

// // Обработчик события радиокнопки выбора способа доставки
// $("input[name='requires_delivery']").change(function() {
//     var selectedValue = $(this).val();
//     // Скрываем или отображаем input ввода адреса доставки
//     if (selectedValue === "1") {
//         $("#deliveryAddressField").show();
//     } else {
//         $("#deliveryAddressField").hide();
//     }
});

const catalog_button = document.getElementById("dropdown-menu_button");
const catalog_menu = document.getElementById("dropdown-menu_list");

catalog_button.addEventListener("click", function() {
    if (catalog_menu.style.display === "none") {
        catalog_menu.style.display = "block"; // Или другой способ отображения
    } else {
        catalog_menu.style.display = "none";
    }
});
