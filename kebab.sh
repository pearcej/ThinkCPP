# for file in *; do
#  echo "$(echo $file | sed -r 's/([A-Z])/-\L\1/g')"
# done

for file in *; do
  mv "$file" -- "$(echo $file | sed -r 's/([A-Z])/-\L\1/g')"
done

for file in *; do
  mv -- "$file" "$(echo $file | sed 's/^-//')"
done