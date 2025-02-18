var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
  },
  spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
      }
  };

django.jQuery(function(){
    django.jQuery('.mask-telephone').mask(SPMaskBehavior, spOptions);
    django.jQuery('.mask-cpf').mask('000.000.000-00', {reverse: true});
    django.jQuery('.mask-cep').mask('00000-000');
    django.jQuery('.vDateField').mask('00/00/0000');
    // django.jQuery('.money').mask('000.000.000.000.000,00', {reverse: true});

    // remover os simbolos dos campos com mask employee_form <- id do modelo geralmente é o nome do modelo
    django.jQuery('#employee_form').submit(function(){
        django.jQuery('#employee_form').find(":input[class*='mask-']").unmask();
    });
})
