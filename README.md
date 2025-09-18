# python-abcd25

# Text Beskrivningar av Kmom01

Berätta hur din utvecklingsmiljö ser ut (när du jobbar med kursen) och om du anpassat den på något särskilt sätt?

Gick det bra att installera kursens utvecklingsmiljö eller var det något som krånglade?

Är du bekant med terminalen och Unix-kommandon sedan tidigare?

Är du bekant med Python sedan tidigare eller har du jobbat med liknande tekniker?

Gick det bra att komma i gång med kursmomentet rent allmänt eller var det något som var lurigt, svårt eller utmanande?

Vilket koncept var det svåraste att förstå i detta kmom? Känner du att du förstår det nu?

Finns det någon det du tycker var extra intressant eller roligt att jobba med i detta kmom?

Borde vi ändra något i kursmomentet för att göra det bättre? Eller utöka information om något?
Vilken är din TIL för detta kmom?

---

I detta kursmoment hade jag svårt med GitHub, repositories och att använda terminalen. Det kändes ovant att köra min kod via terminal i Visual Studio och små misstag gjorde ofta att jag fastnade. Själva uppgifterna var däremot inte lika svåra eftersom jag hade viss erfarenhet från tidigare programmeringsspråk, vilket gjorde att jag lättare förstod kodlogiken. För att lösa problemen med GitHub fick jag söka instruktioner, prova olika kommandon och öva mer praktiskt. Det gav mig en bättre förståelse för hur versionhantering fungerar och varför det är viktigt. En lärdom är att tålamod och träning är avgörande när man möter nya verktyg. Jämfört med mina tidigare erfarenheter fokuserade jag nu inte bara på själva koden, utan också på de verktyg som omger programmeringen. Det här kursmomentet har därför gett mig både nya tekniska färdigheter och mer självförtroende i att hantera problem.
Min akronym för detta moment är python-huka25 alltså huka25..

# Text Beskrivningar av Kmom02

Hur känns syntaxen i Python?

Hur går det med att läsa programmets struktur och vad det gör?

Har du fått en förståelse för hur loopar fungerar?

Vad är skillnaden på en while-loop och en for-loop?

Hur går det med valideringen av uppgifterna?

Hur gick det att utföra uppgifterna, var de enkla eller svåra?

Vilken är din TIL för detta kmom?

---

Jag tycker att Python är rätt enkelt och logiskt. Man behöver inte skriva en massa extra tecken som i andra språk, och bara indenteringen gör att koden blir lättare att läsa.
Det går ganska bra. I min Marvin-kod har jag en meny där användaren väljer vad man vill göra. Det är lätt att se vilken del som körs eftersom jag använder elif för varje alternativ.
Ja, det börjar kännas tydligt. Jag har använt while-loopar när jag inte vet hur länge något ska köras (t.ex. huvudmenyn), och for-loopar när jag ska gå igenom en viss mängd saker (t.ex. siffrorna i ett personnummer).
En while-loop körs så länge villkoret är sant. En for-loop används när man vet hur många gånger något ska upprepas.
här har jag exampel:
While: huvudmenyn, eftersom den ska köra tills man väljer att avsluta.
For: personnummerkontrollen, eftersom jag vet att det alltid är 10 siffror som ska kontrolleras.
Det gick okej, men jag fick lära mig nya saker. I betygsdelen till exempel skrev jag först if procent >= 90:, men ruff check klagade. Då förstod jag att man ska använda konstanter som GRADE_A = 90 och sedan jämföra med dem.
Vissa saker var enkla, som att hälsa eller omvandla grader. Jämföra tal var lite klurigt, eftersom jag behövde tänka på att börja med old_value = None för att inte jämföra mot fel saker. Den svåraste delen var personnummerkontrollen, eftersom jag aldrig jobbat med Luhn-algoritmen tidigare. Det tog tid att förstå reglerna, men när jag väl fattade logiken så gick det bra.
Jag har lärt mig att while och for har olika användningsområden och att det är viktigt att välja rätt. Jag har också lärt mig varför man ska använda konstanter i stället för siffror direkt i koden, och nu kan jag även grunderna i Luhn-algoritmen.
