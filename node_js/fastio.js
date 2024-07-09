const buffer = require('fs').readFileSync('/dev/stdin').toString().split('\n');
// const buffer = require('fs').readFileSync(0).toString().split('\n');

let buffer_ptr = 0
let line_ptr = -1;
let line_buf = '';
const input = function () {
    if (line_buf.length == buffer_ptr) {
        line_buf = readline().trim().split(' ').map(String);
        buffer_ptr = 0;
    }

    return line_buf[buffer_ptr++];
};

const readline = function () {
    line_ptr++;
    if (line_ptr == buffer.length) return undefined;
    buffer_ptr = buffer[line_ptr].length;
    return buffer[line_ptr];
};
