#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [...list];
  let x = newlist.length - 1;
  for (let i = 0; i < newlist.length / 2; i++) {
    const temp = newlist[i];
    newlist[i] = newlist[x];
    newlist[x] = temp;
    x--;
  }
  return (newlist);
};
