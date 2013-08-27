openerp.account_itc = function (instance) {
    instance.web.form.widgets.add('account_itc','openerp.web.form.file');
    instance.web.client_actions.add('account_itc_file', 'instance.account_itc_file.action');
    instance.account_itc.action = function (parent, action) {
        console.log("Executed the action", action);
    };

    instance.web.form.file = instance.web.form.FieldChar.extend(
    {
       template: 'account_itc',

       init: function () {
                 this._super.apply(this, arguments);
                 this._start = null;
       },

       start: function() {
             document.getElementById('fileButton').addEventListener('click', this.file);
        },

        file: function() {
            window.open('http://www.cra-arc.gc.ca/gsthst-internetfiletrans/', '_blank');
        }
    });
};
