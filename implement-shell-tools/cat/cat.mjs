import { program } from "commander";
import { promises as fs } from "node:fs";

program.name("cat");
program.description("simple cat clone");
program.option("-n, --number", "number all output lines");
program.option("-b, --number-nonblank", "number non-empty output lines");
program.argument("[paths...]", "file(s) to process");
program.parse();

const { number, numberNonblank } = program.opts();
const paths = program.args;
