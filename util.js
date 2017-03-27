const path = require('path');

module.exports = {
    makeJoiner: function(prefix, base) {

        return (file) => {
            return prefix + path.join(base, file);
        }
    }
}
