(function (window, document) {
    $(document).ready(function () {
        window.Testr = window.Testr || { util: {}};

        window.Testr.util.isShown = function isShown(el) {
            return $(el).css('display') !== 'none';
        }
    });
})(window, document);
