// Когда html документ готов (прорисован)

// // Берем из разметки элемент по id - оповещения от django
// var notification = $('#notification');
// // И через 7 сек. убираем
// if (notification.length > 0) {
//     setTimeout(function () {
//         notification.alert('close');
//     }, 7000);
// }

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
// });

const catalog_button = document.getElementById("dropdown-menu_button");
const catalog_menu = document.getElementById("dropdown-menu_list");

catalog_button.addEventListener("click", function() {
    if (catalog_menu.style.display === "none") {
        catalog_menu.style.display = "block"; // Или другой способ отображения
    } else {
        catalog_menu.style.display = "none";
    }
});


const form_error_button = document.getElementById("alert_form_errors_btn-close");
const form_error_container = document.getElementById("form_errors_container");

form_error_button.addEventListener("click", function() {
    if (form_error_container.style.display === "block") {
        form_error_container.style.display = "none";
    }
});
