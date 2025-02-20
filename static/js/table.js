$(document).ready(function () {
    // Initialize DataTable
    $('#users-table').DataTable({
        dom: '<"top"f>rt<"bottom"p><"clear">',
        paging: false,
        info: false,
        lengthChange: false,
        language: {
            search: "Chercher:",
            zeroRecords: "Aucun enregistrement correspondant trouvé",
        },
    });

    // Delete Modal Logic
    const deleteModal = $('#deleteModal');

    $('.delete-btn').on('click', function () {
        const userId = $(this).data('id');
        const deleteUrl = "{% url 'dashboard:delete_user' 0 %}".slice(0, -2) + userId;
        $('#confirmDelete').attr('href', deleteUrl);
        deleteModal.modal('show');
    });

    deleteModal.find('.btn-secondary, .close').on('click', function () {
        deleteModal.modal('hide');
    });
});