const fs = require("fs");
const fse = require("fs-extra");
const childProcess = require("child_process");

let buildFolder = "./build";
let outBuildFolder = "../out/build";

//delete folders build & out/build
if (fs.existsSync(buildFolder)) {
    fse.removeSync(buildFolder);
}

if (fs.existsSync(outBuildFolder)) {
    fse.removeSync(outBuildFolder);
}

//Create build and move to out
childProcess.execSync("react-scripts build", { stdio: "inherit" });
fse.moveSync(buildFolder, outBuildFolder, { overwrite: true });
