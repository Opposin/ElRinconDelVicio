const nombreEL = document.querySelector('#apellido_tarjeta');
const apellidoEL = document.querySelector('#nombre_tarjeta');
const numero_tarjetaEL = document.querySelector('#numero_tarjeta');
const codigo_seguridadEL = document.querySelector('#codigo_seguridad');
const fecha_vencimientoEL = document.querySelector('#fecha_vencimiento');

const formulario = document.querySelector('#formulario_tarjeta');

const formularioC = document.getElementById("formulario_tarjeta");


const isRequired = value => value === '' ? false : true;

const isBetween = (length, min, max) => length < min || length > max ? false : true;

const showError = (input, message) => {
    // get the form-field element
    const formField = input.parentElement;
    // add the error class
    formField.classList.remove('success');
    formField.classList.add('error');

    // show the error message
    const error = formField.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    // get the form-field element
    const formField = input.parentElement;

    // remove the error class
    formField.classList.remove('error');
    formField.classList.add('success');

    // hide the error message
    const error = formField.querySelector('small');
    error.textContent = '';
};

const checkName = () => {

    let valid = false;
    const min = 3,
        max = 25;
    const nombre = nombreEL.value.trim();

    if (!isRequired(nombre)) {
        showError(nombreEL, 'El nombre no puede estar vacio.');
    } else if (!isBetween(nombre.length, min, max)) {
        showError(nombreEL, `el nombre debe ser entre ${min} y ${max} caracteres.`)
    } else {
        showSuccess(nombreEL);
        valid = true;
    }
    return valid;
};

const checkSurname = () => {

    let valid = false;
    const min = 3,
        max = 25;
    const apellido = apellidoEL.value.trim();

    if (!isRequired(apellido)) {
        showError(apellidoEL, 'El apellido no puede estar vacio.');
    } else if (!isBetween(apellido.length, min, max)) {
        showError(apellidoEL, `el apellido debe ser entre ${min} y ${max} caracteres.`)
    } else {
        showSuccess(apellidoEL);
        valid = true;
    }
    return valid;
};

const checkCNumber = () => {

    let valid = false;
    const min = 15,
        max = 19;
    const numero_tarjeta = numero_tarjetaEL.value.trim();

    if (!isRequired(numero_tarjeta)) {
        showError(numero_tarjetaEL, 'El numero de tarjeta no puede estar vacio.');
    } else if (isNaN(numero_tarjeta)) {
        showError(numero_tarjetaEL, `La tarjeta solamente puede tener caracteres numericos.`)
    } else if (!isBetween(numero_tarjeta.length, min, max)) {
        showError(numero_tarjetaEL, `Numero de tarjeta no valido.`)
    } else {
        showSuccess(numero_tarjetaEL);
        valid = true;
    }
    return valid;
};

const checkSNumber = () => {

    let valid = false;
    const min = 3,
        max = 3;
    const codigo_seguridad = codigo_seguridadEL.value.trim();

    if (!isRequired(codigo_seguridad)) {
        showError(codigo_seguridadEL, 'El numero de tarjeta no puede estar vacio.');
    } else if (isNaN(codigo_seguridad)) {
        showError(codigo_seguridadEL, `La tarjeta solamente puede tener caracteres numericos.`)
    } else if (!isBetween(codigo_seguridad.length, min, max)) {
        showError(codigo_seguridadEL, `Numero de tarjeta no valido.`)
    } else {
        showSuccess(codigo_seguridadEL);
        valid = true;
    }
    return valid;
};

const checkDate = () => {

    let valid = false;
    const min = 4,
        max = 4;
    const fecha_vencimiento = fecha_vencimientoEL.value.trim();

    if (!isRequired(fecha_vencimiento)) {
        showError(fecha_vencimientoEL, 'El numero de tarjeta no puede estar vacio.');
    } else if (isNaN(fecha_vencimiento)) {
        showError(fecha_vencimientoEL, `La tarjeta solamente puede tener caracteres numericos.`)
    } else if (!isBetween(fecha_vencimiento.length, min, max)) {
        showError(fecha_vencimientoEL, `Numero de tarjeta no valido.`)
    } else {
        showSuccess(fecha_vencimientoEL);
        valid = true;
    }
    return valid;
};

const debounce = (fn, delay = 500) => {
    let timeoutId;
    return (...args) => {
        // cancel the previous timer
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        // setup a new timer
        timeoutId = setTimeout(() => {
            fn.apply(null, args)
        }, delay);
    };
};

formulario.addEventListener('input', debounce(function (e) {
    switch (e.target.id) {
        case 'apellido_tarjeta':
            checkSurname();
            break;
        case 'nombre_tarjeta':
            checkName();
            break;
        case 'numero_tarjeta':
            checkCNumber();
            break;
        case 'codigo_seguridad':
            checkSNumber();
            break;
        case 'fecha_vencimiento':
            checkSNumber();
            break;
    }
}));

formulario.addEventListener('submit', function (e) {
    // prevent the form from submitting
    e.preventDefault();

    // validate forms
    let isNameValid = checkName(),
        isSurnameValid = checkSurname(),
        isCardValid = checkCNumber(),
        isCodeValid = checkSNumber(),
        isDateValid = checkDate();

    let isFormValid = isNameValid &&
        isSurnameValid &&
        isCardValid &&
        isCodeValid &&
        isDateValid;

    // submit to the server if the form is valid
    if (isFormValid) {
        formularioC.submit();
    }
});