import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program.name("ls").description("test").option("-1", "list one file per line").argument("<path>");

program.parse();

const argv = program.args;

if (argv.length != 1) {
  console.error(`Expected exactly 1 argument (a path) to be passed but got ${argv.length}`);
  process.exit(1);
}

const path = argv[0];
const char = program.opts().char;

try {
  const stat = await fs.stat(path);

  if (stat.isDirectory()) {
    const files = await fs.readdir(path);

    for (const file of files) {
      console.log(file);
    }
  } else {
    console.log(path);
  }
} catch (err) {
  console.log(err.message);
}
