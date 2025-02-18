(function ($) {
    $(document).ready(function () {
        function limpa_formulario_cep() {
            // Limpa valores do formulário de CEP.
            $('#id_complement').val('');  // rua
            $('#id_neighborhood').val('');  // bairro
            $('#id_city').val('');  // cidade
            $('#select2-id_address_uf-container').val('');  // estado
            $('#id_number').val('');  // número
        }

        function meu_callback(conteudo) {
            if (!('erro' in conteudo)) {
                // Atualiza os campos com os valores retornados.
                $('#id_complement').val(conteudo.logradouro);
                $('#id_neighborhood').val(conteudo.bairro);
                $('#id_city').val(conteudo.localidade);
                $('#select2-id_address_uf-container').val(conteudo.uf);
            } else {
                // CEP não encontrado.
                limpa_formulario_cep();
                alert('CEP não encontrado.');
            }
        }

        $('#id_cep').on('blur', function () {
            var valor = $(this).val();
            var cep = valor.replace(/\D/g, ''); // Remove caracteres não numéricos.

            if (cep !== '') {
                var validacep = /^[0-9]{8}$/;

                if (validacep.test(cep)) {
                    // Preenche os campos com "..." enquanto consulta o webservice.
                    $('#id_complement').val('...');
                    $('#id_neighborhood').val('...');
                    $('#id_city').val('...');
                    $('#select2-id_address_uf-container').val('...');

                    // Faz a chamada para a API ViaCEP.
                    $.getJSON(`https://viacep.com.br/ws/${cep}/json/?callback=?`, meu_callback);
                } else {
                    limpa_formulario_cep();
                    alert('Formato de CEP inválido.');
                }
            } else {
                limpa_formulario_cep();
            }
        });
    });
})(django.jQuery);
