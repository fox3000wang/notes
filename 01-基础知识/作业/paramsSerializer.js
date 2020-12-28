function paramsSerializer(obj, fathers) {
  let str = ``;
  fathers = fathers ? fathers : [];

  Object.keys(obj).forEach(key => {
    if (obj[key].toString() === `[object Object]`) {
      str += `&${paramsSerializer(obj[key], fathers.concat([key]))}`;
    } else {
      if (fathers.length) {
        let father = `${fathers[0]}`;
        for (let i = 1; i < fathers.length; i++) {
          father += `[${fathers[i]}]`;
        }
        str += `&${father}[${key}]=${obj[key]}`;
      } else {
        str += `&${key}=${obj[key]}`;
      }
    }
  });
  return str.substring(1);
}

const foo = {
  lx: 0,
  from: {
    name: 'abc',
    age: 12,
    bt: {
      0: 1,
      1: 2,
    },
  },
};

console.log(paramsSerializer(foo));
// lx=0&from[name]=abc&from[age]=12&from[bt][0]=1&from[bt][1]=2
