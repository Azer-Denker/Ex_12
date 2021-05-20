const body = $('body');
let Div = $(document.createElement('div'));
Div.addClass('container');
Div.append('<label class="pl-4 pt-5">A:<input id="numberA" type="number" class="form-control mx-3"></label>');
Div.append('<label class="pl-4">B:<input id="numberB" type="number" class="form-control mx-3"></label><br>');
Div.append('<button id="addBtn" class="btn btn-primary ml-5 mr-1" style="margin-left: 15px;">+</button><a>  </a>');
Div.append('<button id="subtractBtn" class="btn btn-primary mr-1">-</button><a>  </a>');
Div.append('<button id="multiplyBtn" class="btn btn-primary mr-1">*</button><a>  </a>');
Div.append('<button id="divideBtn" class="btn btn-primary mr-1">/</button><a>  </a>');
Div.append('<p id="result" class="my-3"></p>');
body.append(Div);


let baseURL = 'http://127.0.0.1:8000/api_v1/';

let numberAInp = $('#numberA');
let numberBInp = $('#numberB');
let addBtn = $('#addBtn');
let subtractBtn = $('#subtractBtn');
let multiplyBtn = $('#multiplyBtn');
let divideBtn = $('#divideBtn');
let result = $('#result')


function jqueryParseData (response, status) {
    result[0].style.color = 'green';
    console.log(status);
    result.html(response['answer']);
}

function jqueryAjaxError(response, status) {
    result[0].style.color = 'red';
    result[0].textContent = 'Ошибка'
    console.log(response);
    console.log(status);
    console.log('error');
}

let calc = function(action) {
    let numberA = numberAInp.val();
    let numberB = numberBInp.val();
    $.ajax({
        method: 'POST',
        url: baseURL + action + '/',
        data: JSON.stringify({"A": numberA, "B": numberB}),
        success: jqueryParseData,
        error: jqueryAjaxError
    })
};

addBtn.on('click', function () {
    calc('add');
});
subtractBtn.on('click', function () {
    calc('subtract');
});
multiplyBtn.on('click', function () {
    calc('multiply');
});
divideBtn.on('click', function () {
    calc('divide');
});
