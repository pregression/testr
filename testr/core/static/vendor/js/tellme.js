$(function () {
    $.feedback({
        ajaxURL: "{% url 'tellme:post_feedback' %}",
        html2canvasURL: "{% static 'tellme/html2canvas.min.js' %}",
        feedbackButton: "#feedback-btn",
        initButtonText: "{% filter escapejs %}{%  include 'tellme/initButtonText.txt' %}{% endfilter %}",
        postHTML: false,
        tpl: {
            description: "{% filter escapejs %}{%  include 'tellme/tpl-description.html' %}{% endfilter %}",
            highlighter: "{% filter escapejs %}{%  include 'tellme/tpl-highlighter.html' %}{% endfilter %}",
                        overview:        "{% filter escapejs %}{%  include 'tellme/tpl-overview.html' %}{% endfilter %}",
                        submitSuccess:"{% filter escapejs %}{%  include 'tellme/tpl-submit-success.html' %}{% endfilter %}",
                        submitError: "{% filter escapejs %}{%  include 'tellme/tpl-submit-error.html' %}{% endfilter %}"
        },
        initialBox: true
    });
});
