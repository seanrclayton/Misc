!/bin/bash
export PATH=$PATH:/usr/local/ops/bin:/usr/java/x64/bin
apps=$1
for i in 1 2; do 
    for app in $apps; do
        pid=$(pgrep -U tomcat -f bin/java.*"$app")
        current_timestamp=$(date +%Y%m%d%H%M%S)
        output_dir=/var/log/$app/threaddumps
        mkdir -p $output_dir || exit 1
        output_file="${output_dir}/${app}-${current_timestamp}-${pid}.threaddump"
        if ! timeout 10 jstack -l $pid > "$output_file"; then
            jstack -F -l $pid > "$output_file";
        fi
        if [ -d $output_dir ]; then
            find $output_dir/ -mmin +60 | compress_slowly
            find $output_dir/ -mtime +7 | rm_slowly
        fi
    done
    if [ $i -eq 1 ]; then sleep 20; fi
done
                                                                                                                             
