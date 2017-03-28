const path = require('path');
const url = require('url');

module.exports = {
    makeJoiner: function(protocol, base) {
        return (file) => {
            var rv = url.format({
                pathname: path.join(base, file),
                protocol,
                slashes: true
            })
            console.log("URL", rv);
            return rv;
        }
    }
}
