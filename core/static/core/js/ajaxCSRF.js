(function (window, document) {
    $(document).ready(function () {
        /**
         * @returns {boolean}
         */
        function cookiesEnabled() {
            return document.cookie && document.cookie !== "";
        }

        /**
         * @returns {Array}
         */
        function getCookies() {
            if (cookiesEnabled()) {
                return document.cookie.split(";");
            }
            return [];
        }

        /**
         * @param {string} name 
         * @param {string} cookie 
         * @returns {boolean}
         */
        function desiredCookie(name, cookie) {
            return cookie.substring(0, name.length + 1) === name + "=";
        }

        /**
         * @param {string} cookie 
         * @param {number} idx 
         * @returns {string}
         */
        function getCookieValue(cookie, idx) {
            return decodeURIComponent(cookie.substring(idx));
        }

        /**
         * @param {string} name 
         * @returns {string|boolean}
         */
        function getCookie(name) {
            return getCookies().find(function (cookie) {
                if (desiredCookie(name, cookie)) {
                    return getCookieValue(cookie, name.length + 1);
                }
                return false;
            });
        }

        /**
         * @param {string} method 
         * @returns {boolean}
         */
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        /**
         * @param {string} token 
         * @returns {void}
         */
        function applyCSRFToken(token) {
            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", token);
                    }
                }
            });
        }

        var csrftoken = getCookie("__Host-csrftoken") || $("[name=csrfmiddlewaretoken]").val();
        if (csrftoken) {
            applyCSRFToken(csrftoken);
        }
    });
}(window, document));
