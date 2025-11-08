Working with React
====================================================================
> Description of technical aspects of React. How it compiles. 

Installing
====================================================================
Just download the tic tac toe example and follow this document.

Compiling
====================================================================
To ease the analysis I attached a debugger to the `npm-cli.js` file, which is
the direct link to the `npm` command. Moreover, the shebang line was updated 
to this

    #!/usr/bin/env -S node --inspect-brk

So each time that we run npm something the script will wait for us to connect
a debugging client. 

How the compilation goes
---------------------------------
1. Somehow you get the `start.js` script executed from `npm-cli.js`. The main aim
of this guide is to understand how React compiles. Is the `start.js` where you 
will find the procedure to compile.
2. Inside of `start.js` you will find the instantiation of the compiler object,
which most important parameter is the `webpack` module. The instantiation happens in the 
`createCompiler` function brought by `WebpackDevServerUtils.js`.
3. The webpack object passed as argument is the result of the `require('webpack')` import call.
This executes not the package called _webpack_ but the script called `webpack.js` that resides
inside the package. The webpack object at the end is a function that returns a `Compiler` object
defined in the same _webpack_ package. Here you can get confused with the `./bin/webpack.js`, `./lib/webpack.js` and the `./lib/index.js` because, because it is not clear which one is the entry point of the package. However, when you check the `package.json` file you will find that the entry point is `./lib/index.js` file, and withing this file you _require_ the `webpack.js` file within the same folder. `./lib/index.js` file, and withing this file you _require_ the `webpack.js` file within the same folder.
4. We jump directly to analyze the `Compiler` object. At first it seems that we are doing this obscure jumps, but no. when we call `webpack(config)` after importing it we really are calling the function we just describe before. 
The Compiler constructor defines several hook and the class itself defines several instance methods. Because their names, I analize `emitAssets(...)` and `compile(...)` functions. At that point I put some breakpoints and analize the stack.
5. The `compile(callback)` function in `Compile` mostly coordinates some of the hooks of the compiler.It is important to note that the hooks are created on demand and has an added complexity in order to get the correct hooks defined. 5. The `compile(callback)` function in `Compile` mostly coordinates some of the hooks of the compiler.It is important to note that the hooks are created on demand and has an added complexity in order to get the correct hooks defined. 5. The `compile(callback)` function in `Compile` mostly coordinates some of the hooks of the compiler.It is important to note that the hooks are created on demand and has an added complexity in order to get the correct hooks defined. 5. The `compile(callback)` function in `Compile` mostly coordinates some of the hooks of the compiler.It is important to note that the hooks are created on demand and has an added complexity in order to get the correct hooks defined. 5. The `compile(callback)` function in `Compile` mostly coordinates some of the hooks of the compiler.It is important to note that the hooks are created on demand and has an added complexity in order to get the correct hooks defined. 
6. 


Other
====================================================================

Tracking log
====================================================================
### 240816
This is the first time trying to work with php technology

References
====================================================================
[1]: https://www.gnu.org/software/bash/manual/bash.html#Positional-Parameters
[2]: https://docs.docker.com/engine/reference/builder/#entrypoint
[3]: https://zookeeper.apache.org/doc/r3.9.1/javaExample.html
