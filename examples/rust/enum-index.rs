#![allow(dead_code)]

fn main() {

//x description="enum with indices"

//x step={
enum Number {
    Zero,
    One,
    Two,
}
//x }

//x post={
println!("two is {}", Number::Two as i32);
//x }

}

