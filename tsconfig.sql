create text search dictionary us_spending ( template = simple, stopwords = US_Spending );
create text search configuration us_spending ( copy = simple );
alter text search configuration us_spending alter mapping for asciiword with us_spending;
commit;
