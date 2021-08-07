function hammstring(a,b)
    return length(a) == length(b) ? sum([a[i] != b[i] for i in 1:length(a)]) : length(a) > length(b) ? sum([a[i] != b[i] for i in 1:length(b)]) : sum([a[i] != b[i] for i in 1:length(a)])
end
println("NAME:Akinwale Akinjiola")
println("EMAIL:akinjil@gmail.com")
println("SLACK:@Akinwale")
println("BIOSTACK:DataScience")
println("TWITTER:@Akinwale_shines")
println(string("HAMMSTRING:", hammstring("@Akinwale", "@Akinwale_shines")))
