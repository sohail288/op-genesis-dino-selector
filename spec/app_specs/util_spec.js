var util = require('../../util');
var path = require('path');

describe('util', function() {

    it('joins files correctly', function() {
        var joiner = util.makeJoiner('file://', __dirname);
        var result = 'file://' + path.resolve('spec/app_specs/test');
        expect(joiner('test')).toEqual(result);
    })
});
