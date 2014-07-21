require 'httparty'
require 'pp'


new_array = []
file = File.open('thing.json', 'r')
JSON.parse(file.read)['log']['entries'].each do |request|
urls = request['request']['url']
if urls =~ /jpg/
new_array << urls
end
end

new_array.each do |x|

`wget #{x}`
