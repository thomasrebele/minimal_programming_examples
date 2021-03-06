#![allow(unused_variables)]

fn main() {

//x description="define a channel (2)"

//x step={
use std::sync::mpsc::*;
//x }

//x post={
let (s, r) : (Sender<i32>, Receiver<i32>) = channel();

std::thread::spawn(
    move || s.send(1)
    // send does not block
);

let a = r.recv();
//x }

}
