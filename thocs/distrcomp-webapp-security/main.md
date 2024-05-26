Security on distributed application sessions
===========================================================
> In this guide I will share some resources and some background thant can help you to clarify why the classical way on handling session is not safe and how JWT technology helps to avoid security holes.

Background
===========================================================
Today I was trying to implement JWT to a sample backend system written in Spring Boot. Since Spring Boot does not provide a solution out of the box, I must first to understand how the basic system works [1] and compare that with the OWASP [2] cheat sheet recomendations [2].
After read that you can realize easily how JWT [3] works and what is its main purpose in the authentication field.


[1](https://docs.spring.io/spring-session/reference/guides/boot-jdbc.html#httpsession-jdbc-boot-how)

[2](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html#local-storage)

[3](https://jwt.io/introduction)
