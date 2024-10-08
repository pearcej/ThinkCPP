# for file in *; do
#  echo "$(echo $file | sed -r 's/([A-Z])/-\L\1/g')"
# done

for file in *; do
  mv -f -- "$file" "$(echo $file | sed 's/_/-/')"
  # echo "$(echo $file | sed 's/_/-/')"
done
# echo "------------------------------------------"

for file in *; do
  mv -f -- "$file" "$(echo $file | sed -r 's/([A-Z])/-\L\1/g')"
  # echo $file | sed -r 's/([A-Z])/_\L\1/g'
done

# echo "------------------------------------------"
for file in *; do
  mv -f -- "$file" "$(echo $file | sed 's/^-//')"
  #echo $file | sed 's/^_//'
done
# echo "------------------------------------------"
# for file in *; do
#   #mv -f -- "$file" "$(echo $file | sed 's/^-//')"
#   echo "_${file}"
# done