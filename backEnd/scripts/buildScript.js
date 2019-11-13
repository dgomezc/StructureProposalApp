const fs = require("fs");
const fse = require("fs-extra");
const path = require("path");

let codeFolder = "../backEnd";
let outFolder = "../out";

//Clean build directory
fs.readdirSync(outFolder)
  .filter(item => item !== "build")
  .forEach(item => {
    item = path.join(outFolder, item);
    fse.removeSync(item);
  });

//backend
//TODO: Filter yarn.lock file too
const filterFunc = (src, dest) => {
  let validFile =
    src.indexOf("node_modules") < 0 &&
    src.indexOf("scripts") < 0 &&
    src.indexOf("package-lock") < 0;
  return validFile;
};

fse.copySync(codeFolder, outFolder, filterFunc);
