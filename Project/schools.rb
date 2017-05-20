schools = School.all

for school in schools
	puts "#{school.en_name}    #{school.ar_name}      #{school.routes.count}"