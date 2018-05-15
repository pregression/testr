(function (window, document) {
    $(document).ready(function () {
        /**
         * Click handler to show/hide menu
         */
        $("#profileIcon").click(function onClick() {
            var $menu = $("#menu");
            window.Testr.util.isShown($menu)
                ? $menu.hide()
                : $menu.show();
        });

        /**
         * Public API
         */
        window.Testr.Header = window.Testr.Header || {};
    });
}(window, document));
