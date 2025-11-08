TypeScript basics
====================================================================
> Ideas about the first approach to TypeScript while working with opensource
projects in JavaScript (e.g. React). 


Syntax 
====================================================================
It has been a while that I encounter /* comments in javascript sources. They
are borrowed from TypeScript JSDoc Syntax. In particular the ones I see that
have broader use are something like this:
    
    ~~~ts
    /**
	 * @param {WebpackOptions | (ReadonlyArray<WebpackOptions> & MultiCompilerOptions)} options options
	 * @param {Callback<Stats> & Callback<MultiStats>=} callback callback
	 * @returns {Compiler | MultiCompiler | null} Compiler or MultiCompiler
	 */
    ~~~

The operators `&`, `|` and `<>` are documented here [1]. Basically the mean respectively:
the compound type, the one or another type and somekind of generics (~50%sure)

The handbook is useful
--------------------------------
The 'handbook' has everything, can be found here [2]. Here I will left the most recurring visits:

### Several ways to declare a type [3]
Also here is included how to default an attribute with ?



other
---------------------------------
This [documentation][1] 


Other
====================================================================

Tracking log
====================================================================
### 240816
This is the first time trying to work with php technology

References
====================================================================
[1]: https://www.typescriptlang.org/docs/handbook/unions-and-intersections.html
[2]: https://www.typescriptlang.org/docs/handbook/intro.html 
[3]: https://www.typescriptlang.org/docs/handbook/2/objects.html
